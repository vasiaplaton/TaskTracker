from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from . import schemas
from .config import settings
from .crud import get_user
from .database import get_db
from .schemas import *
from fastapi import APIRouter
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Annotated, Union
from fastapi import Depends, HTTPException, status

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_HOURS = 24


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
    expires: datetime
    type_t: str


class AuthRes(BaseModel):
    access_token: Token
    refresh_token: Token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str) -> Union[bool, User]:
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm


def create_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    print(datetime.utcnow())
    print(expire)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_access_token(data: dict) -> Token:
    to_encode = data.copy()
    to_encode.update({"type": "access"})
    token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_token(
        data=to_encode, expires_delta=token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


def create_refresh_token(data: dict) -> Token:
    # TODO: add single time use check
    to_encode = data.copy()
    to_encode.update({"type": "refresh"})
    token_expires = timedelta(hours=REFRESH_TOKEN_EXPIRE_HOURS)
    access_token = create_token(
        data=to_encode, expires_delta=token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


def check_token(token: str, needed_type: str, db: Session) -> Union[User, None]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        expires: datetime = payload.get("exp")
        type_t: str = payload.get("type")
        if email is None:
            return None
        token_data = TokenData(email=email, expires=expires, type_t=type_t)
        token_data.expires = token_data.expires.replace(tzinfo=None)

    except JWTError:
        return None

    print(token_data.type_t)
    if token_data.type_t != needed_type:
        return None
    if datetime.utcnow() > token_data.expires:
        return None
    user = get_user(db, email=token_data.email)
    if user is None:
        return None
    return user


def check_access_token(token: str, db: Session) -> Union[User, None]:
    return check_token(token, "access", db)


def check_refresh_token(token: str, db: Session) -> Union[User, None]:
    # TODO: add single time use check
    return check_token(token, "refresh", db)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = check_access_token(token, db)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    # if current_user.disabled:
    #    raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token")
async def login_for_tokens(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                           db: Session = Depends(get_db)) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    data = {"sub": user.email}

    access_token = create_access_token(data)
    refresh_token = create_refresh_token(data)

    return access_token
    # return AuthRes(access_token=access_token, refresh_token=refresh_token)


@router.post("/refresh")
async def get_access_token(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)) -> Token:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = check_refresh_token(token, db)
    print(user)
    if user is None:
        raise credentials_exception

    data = {"sub": user.email}
    access_token = create_access_token(data)

    return access_token


@router.get("/users/me/")
async def read_users_me(current_user: Annotated[schemas.User, Depends(get_current_active_user)]) -> schemas.User:
    return current_user

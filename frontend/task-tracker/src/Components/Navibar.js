import React, {useEffect, useState} from "react";
import {Navbar, Nav, Button, Modal, Form, Alert} from "react-bootstrap";


export function Navibar() {
    const [show, setShow] = useState(false)
    const [isAuth, setIsAuth] = useState(false);
    const [showNotification, setShowNotification] = useState(false);
    const [user, setUser] = useState(null);

    const handleClose = () => {
        setShow(false)
        setShowNotification(false);
    }

    const handleShow = () => {
        setShow(true)
    }

    const userUpdate = () => {
        let isAuthR = localStorage.getItem('isAuth')
        if(isAuthR == null || !isAuthR) {
            setIsAuth(false)
        }
        else {
            fetch('http://127.0.0.1:8008/users/me', {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
                },
            })
                .then(response => {
                    if (!response.ok) {
                        setIsAuth(false)
                        return;
                    }
                    return response.json();
                })
                .then(userData => {
                    // Set the user state with the retrieved data
                    setUser(userData);
                }).finally(() => {
                if(user != null){
                    setIsAuth(true)
                }
            })
        }
    }

    const handleLogout = () => {
        localStorage.setItem('accessToken', "");
        localStorage.setItem('isAuth', false);
        userUpdate();
    }



    useEffect(() => {
       userUpdate();
    })

    const handleLogin = () => {
        const email = document.getElementById('formBasicEmail').value;
        const password = document.getElementById('formBasicPassword').value;
        console.log(email)
        console.log(password)

        const formData = new URLSearchParams();
        formData.append('username', email);
        formData.append('password', password);

        fetch('http://127.0.0.1:8008/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData.toString(),
        })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the server as needed
                // Handle the response from the server as needed
                console.log(data);

                // Save the access token and isAuth in localStorage
                localStorage.setItem('accessToken', data.access_token);
                localStorage.setItem('isAuth', true);

                setIsAuth(true);

                // Show notification
                setShowNotification(true);

                handleClose(); // Close the modal after successful login
            })
            .catch(error => {
                // Handle errors
                console.error('Error:', error);
                setIsAuth(false);
                setShowNotification(true);
            });

        userUpdate();
    };


    return (
        <>
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand> TaskTracker</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href="/">Home</Nav.Link>
                    <Nav.Link href="/users">Users</Nav.Link>
                    <Nav.Link href="/notes">Notes</Nav.Link>
                    <Nav.Link href="/about">About</Nav.Link>

                </Nav>
                <Nav>
                    {isAuth ?
                        <>
                        {user != null ?
                            <Nav.Link href="/users">{user.email}</Nav.Link> : null
                        }

                            <Button variant="primary" onClick={handleLogout}> Log Out</Button>
                        </>
                        :

                        <Button variant="primary" className="me-2" onClick={handleShow}>Log In</Button>
                    }
                </Nav>
            </Navbar.Collapse>
        </Navbar>
        <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
                <Modal.Title>
                    Log in
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group controlId="formBasicEmail">
                        <Form.Label>
                            Email address
                        </Form.Label>
                        <Form.Control type="email" placeholder="Enter email"/>
                        <Form.Text className="text-muted">

                        </Form.Text>
                    </Form.Group>

                    <Form.Group controlId="formBasicPassword">
                        <Form.Label>
                            Password
                        </Form.Label>
                        <Form.Control type="password" placeholder="Enter password"/>
                    </Form.Group>

                    <Form.Group controlId="formBasicCheckbox">
                        <Form.Check type="checkbox" label="Remember me"/>
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={handleClose}>
                    Close
                </Button>
                <Button variant="primary" onClick={handleLogin}>
                    Login
                </Button>
            </Modal.Footer>
        </Modal>

            {/* Notification */}
            <Alert variant={isAuth ? 'success' : 'danger'} show={showNotification} onClose={() => setShowNotification(false)} dismissible>
                {isAuth ? 'Login successful!' : 'Login failed. Please check your credentials.'}
            </Alert>
        </>
    )
}
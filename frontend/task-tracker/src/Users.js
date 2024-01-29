import React, { useEffect, useState } from "react";

const Users = () => {
    const [user, setUser] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Check if there is a token in localStorage
        const storedToken = localStorage.getItem('accessToken');

        if (storedToken) {
            // If a token is found, make a request to /users/me
            fetch('http://127.0.0.1:8008/users/me', {
                headers: {
                    Authorization: `Bearer ${storedToken}`,
                },
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Failed to fetch user information');
                    }
                    return response.json();
                })
                .then(userData => {
                    // Set the user state with the retrieved data
                    setUser(userData);
                })
                .catch(error => {
                    console.error('Error fetching user information:', error);
                    setError(error.message);
                });
        } else {
            // If no token is found, set an error
            setError('Token not found in localStorage');
        }
    }, []);

    if (error) {
        return <h1>Error: {error}</h1>;
    }

    if (!user) {
        return <h1>Loading...</h1>;
    }

    return (
        <div>
            <h1>User Information</h1>
            <p>User ID: {user.id}</p>
            <p>Email: {user.email}</p>
            <p>Username: {user.username}</p>
            <p>Username: {user.role}</p>
            {/* Display other user information as needed */}
        </div>
    );
}

export default Users;

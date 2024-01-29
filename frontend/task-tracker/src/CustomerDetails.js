// CustomerDetails.js

import React, {useEffect, useState} from 'react';
import {Modal, Button, ListGroup} from 'react-bootstrap';

const CustomerDetails = ({ customer, showModal, handleClose }) => {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        // Fetch tasks for the current user associated with the selected customer
        fetch(`http://127.0.0.1:8008/customer/${customer.id}/tasks`, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
            },
        })
            .then((response) => response.json())
            .then((data) => setTasks(data))
            .catch((error) => console.error('Error fetching tasks for customer:', error));
    }, [customer.id]);

    return (
        <Modal show={showModal} onHide={handleClose}>
            <Modal.Header closeButton>
                <Modal.Title>Customer Details: {customer.name}</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <p>Contact: {customer.contact}</p>
                <p>ID: {customer.id}</p>
                <p>User ID: {customer.user_id}</p>
                <hr />
                <p>Tasks for Current User:</p>
                <ListGroup>
                    {tasks.map((task) => (
                        <ListGroup.Item key={task.id}>{task.name}</ListGroup.Item>
                    ))}
                </ListGroup>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={handleClose}>
                    Close
                </Button>
            </Modal.Footer>
        </Modal>
    );
};

export default CustomerDetails;

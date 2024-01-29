import React, { useEffect, useState } from "react";
import { Card, Badge, Container, Row, Col } from "react-bootstrap";
import NotesModal from "./NotesModal";
import CustomerDetails from "./CustomerDetails";

const TaskCard = ({ task }) => {
    const [showNotesModal, setShowNotesModal] = useState(false);
    const [showCustomerDetails, setShowCustomerDetails] = useState(false); // State for customer details modal

    const handleShowNotesModal = () => setShowNotesModal(true);
    const handleCloseNotesModal = () => setShowNotesModal(false);

    const handleShowCustomerDetails = () => setShowCustomerDetails(true);
    const handleCloseCustomerDetails = () => setShowCustomerDetails(false);

    const getTaskStatusColor = () => {
        if (task.status_completed === "Completed") {
            return "success";
        } else if (task.status_completed === "New") {
            return "primary";
        } else if (new Date(task.deadline) < new Date()) {
            return "danger";
        } else {
            return "primary";
        }
    };

    return (
        <Card className="mb-3" style={{ maxWidth: "400px" }}>
            <Card.Header>
                <Badge variant={getTaskStatusColor()} className={'mr-2 bg-'+getTaskStatusColor()}>
                    {task.status_completed}
                </Badge>
                <strong>{task.name}</strong>
            </Card.Header>
            <Card.Body>
                <Card.Text>{task.description}</Card.Text>
                <Container>
                    <Row>
                        <Col>
                            <strong>Deadline:</strong> {new Date(task.deadline).toLocaleString()}
                        </Col>
                        <Col>
                            <strong>Payment:</strong> {task.payment} USD
                        </Col>
                    </Row>
                </Container>
            </Card.Body>
            <Card.Footer>
                <Badge variant="info" className="mr-2" onClick={handleShowCustomerDetails}>
                    Customer: {task.customer.name}
                </Badge>
                {task.notes.length > 0 && (
                    <Badge variant="warning" onClick={handleShowNotesModal}>
                        {task.notes.length} {task.notes.length === 1 ? "Note" : "Notes"}
                    </Badge>
                )}
            </Card.Footer>

            <NotesModal task={task} showModal={showNotesModal} handleClose={handleCloseNotesModal} />
            <CustomerDetails
                customer={task.customer}
                showModal={showCustomerDetails}
                handleClose={handleCloseCustomerDetails}
            />
        </Card>
    );
};

const Home = () => {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        // Fetch tasks from the server
        fetch('http://127.0.0.1:8008/tasks', {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
            },
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch tasks');
                }
                return response.json();
            })
            .then(data => {
                setTasks(data);
            })
            .catch(error => {
                console.error('Error fetching tasks:', error);
            });
    }, []);

    return (
        <div>
            <h1>Home</h1>
            {tasks.map(task => (
                <TaskCard key={task.id} task={task} />
            ))}
        </div>
    );
};

export default Home;

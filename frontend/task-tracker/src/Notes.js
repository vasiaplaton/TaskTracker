import React, { useState, useEffect } from 'react';
import { Card, Badge, Container, Row, Col, Form } from 'react-bootstrap';
import NotesModal from './NotesModal';
import CustomerDetails from './CustomerDetails';

const NoteCard = ({ note }) => {
    const [showNotesModal, setShowNotesModal] = useState(false);
    const [showCustomerDetails, setShowCustomerDetails] = useState(false);

    const handleShowNotesModal = () => setShowNotesModal(true);
    const handleCloseNotesModal = () => setShowNotesModal(false);

    const handleShowCustomerDetails = () => setShowCustomerDetails(true);
    const handleCloseCustomerDetails = () => setShowCustomerDetails(false);

    return (
        <Card className="mb-3" style={{ maxWidth: '400px' }}>
            <Card.Header>
                <strong>{note.title}</strong>
            </Card.Header>
            <Card.Body>
                <Card.Text>{note.description}</Card.Text>
                <Container>
                    <Row>
                        <Col>
                            <strong>Created at:</strong> {new Date(note.created_at).toLocaleString()}
                        </Col>
                    </Row>
                </Container>
            </Card.Body>
            <Card.Footer>
                <Badge variant="info" className="mr-2" onClick={handleShowCustomerDetails}>
                    Task ID: {note.task_id}
                </Badge>
                <Badge variant="warning" onClick={handleShowNotesModal}>
                    Edit Note
                </Badge>
            </Card.Footer>

        </Card>
    );
};

const NotesPage = () => {
    const [notes, setNotes] = useState([]);
    const [searchText, setSearchText] = useState('');

    useEffect(() => {
        // Fetch notes from the server based on the search text
        //     <NotesModal task={note.task} note={note} showModal={showNotesModal} handleClose={handleCloseNotesModal} />
        fetch(`http://127.0.0.1:8008/notes-filter?search_text=${searchText}`, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
            },
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch notes');
                }
                return response.json();
            })
            .then(data => {
                console.log(data)
                setNotes(data);
            })
            .catch(error => {
                console.error('Error fetching notes:', error);
            });
    }, [searchText]);

    return (
        <div>
            <h1>Notes</h1>
            <Form>
                <Form.Group controlId="formSearchText">
                    <Form.Control
                        type="text"
                        placeholder="Search by text"
                        value={searchText}
                        onChange={e => setSearchText(e.target.value)}
                    />
                </Form.Group>
            </Form>
            {notes.map(note => (
                <NoteCard key={note.id} note={note} />
            ))}
        </div>
    );
};

export default NotesPage;

import React, { useState } from 'react';
import { Modal, Button, Form } from 'react-bootstrap';

const AddNoteModal = ({ showModal, handleClose, handleAddNote }) => {
    const [newNote, setNewNote] = useState({ title: '', description: '', scheduled_at: '' });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewNote((prevNote) => ({ ...prevNote, [name]: value }));
    };

    const handleAddNoteClick = () => {
        handleAddNote(newNote);
        setNewNote({ title: '', description: '', scheduled_at: '' });
    };

    return (
        <Modal show={showModal} onHide={handleClose}>
            <Modal.Header closeButton>
                <Modal.Title>Add New Note</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group controlId="noteTitle">
                        <Form.Label>Title</Form.Label>
                        <Form.Control
                            type="text"
                            name="title"
                            value={newNote.title}
                            onChange={handleInputChange}
                        />
                    </Form.Group>
                    <Form.Group controlId="noteDescription">
                        <Form.Label>Description</Form.Label>
                        <Form.Control
                            as="textarea"
                            rows={3}
                            name="description"
                            value={newNote.description}
                            onChange={handleInputChange}
                        />
                    </Form.Group>
                    <Form.Group controlId="noteScheduledAt">
                        <Form.Label>Scheduled Date</Form.Label>
                        <Form.Control
                            type="text"
                            name="scheduled_at"
                            value={newNote.scheduled_at}
                            onChange={handleInputChange}
                        />
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={handleClose}>
                    Close
                </Button>
                <Button variant="primary" onClick={handleAddNoteClick}>
                    Add Note
                </Button>
            </Modal.Footer>
        </Modal>
    );
};

export default AddNoteModal;

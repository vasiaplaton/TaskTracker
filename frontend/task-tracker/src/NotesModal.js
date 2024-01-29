import React, { useState, useEffect } from 'react';
import { Modal, Button, Form } from 'react-bootstrap';
import AddNoteModal from './AddNoteModal';  // Import the AddNoteModal component

const NotesModal = ({ task, showModal, handleClose }) => {

    const [notes, setNotes] = useState([]);
    const [showAddNoteModal, setShowAddNoteModal] = useState(false);  // State to control the visibility of the AddNoteModal

    const handleDeleteNote = (noteId) => {
        // Perform DELETE request to delete the note
        fetch(`http://127.0.0.1:8008/notes/${noteId}`, {
            method: 'DELETE',
            headers: {
                Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
            },
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to delete note');
                }
                // Update notes state by removing the deleted note
                setNotes(prevNotes => prevNotes.filter(note => note.id !== noteId));
            })
            .catch(error => console.error('Error deleting note:', error));
    };

    useEffect(() => {
        // Fetch notes for the specific task
        fetch(`http://127.0.0.1:8008/notes?task_id=${task.id}`, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
            },
        })
            .then(response => response.json())
            .then(data => setNotes(data))
            .catch(error => console.error('Error fetching notes:', error));
    }, [task.id]);

    const handleAddNote = (newNote) => {
        // Perform POST request to add a new note
        fetch('http://127.0.0.1:8008/notes', {
            method: 'POST',
            headers: {
                Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                task_id: task.id,
                title: newNote.title,
                description: newNote.description,
            }),
        })
            .then(response => response.json())
            .then(data => {
                // Update notes state with the new note
                setNotes([...notes, data]);
                // Close the AddNoteModal
                setShowAddNoteModal(false);
            })
            .catch(error => console.error('Error adding note:', error));
    };

    return (
        <>
            <Modal show={showModal} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Notes for Task: {task.name}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    {notes.map(note => (
                        <div key={note.id}>
                            <h5>{note.title}</h5>
                            <p>{note.description}</p>
                            <small>Created at: {new Date(note.created_at).toLocaleString()}</small>
                            <Button variant="danger" size="sm" onClick={() => handleDeleteNote(note.id)}>
                                Delete
                            </Button>
                            <hr />
                        </div>
                    ))}
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="primary" onClick={() => setShowAddNoteModal(true)}>
                        Add Note
                    </Button>
                </Modal.Footer>
            </Modal>

            {/* Render the AddNoteModal */}
            <AddNoteModal
                showModal={showAddNoteModal}
                handleClose={() => setShowAddNoteModal(false)}
                handleAddNote={handleAddNote}
            />
        </>
    );
};

export default NotesModal;

import React, { useState, useEffect } from 'react';
import { ListGroup } from 'react-bootstrap';

import {getApi} from './ApiContext'

const YourComponent = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(getApi() + '/technologies/');
                const result = await response.json();
                setData(result);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []); // Зависимость пуста, чтобы эффект выполнялся только один раз при монтировании

    return (
        <div>
            <h1>Technologies</h1>
            <ListGroup>
                {data.map((tech) => (
                    <ListGroup.Item key={tech.id}>
                        <strong>{tech.name}:</strong> {tech.description}
                    </ListGroup.Item>
                ))}
            </ListGroup>
        </div>
    );
};

export default YourComponent;
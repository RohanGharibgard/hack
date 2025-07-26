import React, { useState } from 'react'
import { socket } from './App';

function handleSend(message) {
    socket.emit('display', message);
}
export default function Message() {
    const [message, setMessage] = useState("");

    return (
        <div style={{textAlign: 'center'}}>
            <input type="text" value={message} placeholder='Message' onChange={
                (e) => {
                    setMessage(e.target.value)
                }
             } />
            <button type="button" onClick={() => handleSend(message)}>Send</button>
        </div>
    )
}

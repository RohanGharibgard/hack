import React, {useState, useEffect} from "react";
import {AppContext, socket} from "./App";


function handleClick() {
  console.log("Requesting to take picture...")
  socket.emit('take_picture')
}
export function Camera() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [imagePath, setImagePath] = useState("");

  useEffect(() => {
    socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      console.log("Picture status:");
      console.log(pictureStatus);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });

    return () => {
      socket.off('picture_taken');
    };
  }, []);

  return (
    <div className="camera" style={{textAlign: 'center', height: 700, width: 'auto'}}>
        <img src={pictureStatus !== "" ? imagePath : "null_image.jpeg"} height='70%'></img>
        <div>
            <button onClick={(e) => handleClick()}>Take photo</button>
        </div>
    </div>


  )
}

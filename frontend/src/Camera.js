import React, {useState, useEffect} from "react";
import {AppContext, socket} from "./App";
import imagePath from "./downloaded_image.jpg"
import audioPath from "./image_analysis.mp3"

export function Camera() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [prompt, setPrompt] = useState("");
  const [analysisStatus, setAnalysisStatus] = useState("");
  const [audioUrl, setAudioUrl] = useState("");

  function takePicture() {
    console.log("Requesting to take picture...");
    socket.emit("take_picture");
    setAnalysisStatus("");
  }

  function analyzeImage(prompt) {
    socket.emit('analyze_picture', prompt);
  }

  useEffect(() => {
    socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
    });

    socket.on('picture_analyzed', data => {
      setAnalysisStatus(data.message);
      setAudioUrl(data.audioPath); // data.audioPath should be the URL or blob of the new MP3
    });

    return () => {
      socket.off('picture_taken');
      socket.off('picture_analyzed');
    };
  }, []);

  useEffect(() => {
    console.log("Picture status:");
    console.log(pictureStatus);

  }, [pictureStatus])

  return (
    <div className="camera" style={{textAlign: 'center', width: '700'}}>
      <img src={pictureStatus !== "" ? imagePath : "null_image.jpeg"} width='70%' />
      <div>
        <button onClick={(e) => takePicture()} height="auto">Take photo</button>
      </div>
      <div>
        <input type='text' value={prompt} onChange={(e) => setPrompt(e.target.value)} placeholder="Prompt"/>
        <button onClick={(e) => {
          if (prompt) {
            if (pictureStatus)
              analyzeImage(prompt);
            else
              alert('No image available.');
            setPrompt("");
          }
          else {
            alert("No prompt chosen");
          }
        }}>Analyze Image</button>
  
          { analysisStatus && audioUrl &&
            <audio controls preload="auto" key={audioUrl}>
              <source src={audioUrl} type="audio/mpeg" />
            </audio>
        }
        
      </div>
      
    </div>


  )
}

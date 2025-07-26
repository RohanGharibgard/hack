import React, { useState, useEffect, useContext, createContext } from "react";
import io from 'socket.io-client';
import './App.css';
import { Camera } from "./Camera";
import Message from "./Message"
import SensorData from "./SensorData"
export const socket = io('http://localhost:8000');
export const AppContext = createContext(null);

const logoImg = "Fabulous4_logo.jpg"

function App() {

  return (
    <AppContext.Provider value={{
    }}>
      <div className="app">
        <div>
          <h1 style={{ display: 'inline-block', paddingRight: '20pt'}}>Fabulous4</h1>
          <img src={logoImg} width="50pt"/>
        </div>
        
        <div style={{ display: 'inline-block'}}>
          <Camera />
        </div>
        <div style={{ display: "inline-block", position: 'relative', bottom: 100}}>
          <div style={{textAlign: 'center', width: 'auto'}}>
            <SensorData />
          </div>    
        </div>
        <Message />
      </div>
    </AppContext.Provider>
  );
}

export default App;

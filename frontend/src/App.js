import React, { useState, useEffect, useContext, createContext } from "react";
import io from 'socket.io-client';
import './App.css';
import { Camera } from "./Camera";

export const socket = io('http://localhost:8000');
export const AppContext = createContext(null);

function App() {

  return (
    <AppContext.Provider value={{
    }}>
    <div className="app">
      <div>
        <h1>Fabulous4</h1>
      </div>
      <Camera />
    </div>
    </AppContext.Provider>
  );
}

export default App;

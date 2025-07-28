import React, { useState } from 'react'
import { socket } from './App'
import { useEffect } from 'react';

export default function SensorData() {
  const [ultrasonic, setUltrasonic] = useState("");
  const [temp, setTemp] = useState("");
  const [humidity, setHumidity] = useState("");
  const [light, setLight] = useState("");
  const [sensorData, setSensorData] = useState({
    ultrasonic: "Hi",
    temp: "What",
    humidity: "",
    light: ""
  });

  useEffect(() => {
    socket.on('distance', (data) => {
      setUltrasonic(data);
    });

    socket.on('temp', (data) => {
      setTemp(data);

    });

    socket.on('humidity', (data) => {
      setHumidity(data);

    });

    socket.on('light', (data) => {
      setLight(data)
    });

    return () => {
      socket.off('distance');
      socket.off('humidity');
      socket.off('temp');
      socket.off('light');
    }
  }, []);


  return (
    <div>
      <table style={{ textAlign: 'left' }}>
        <tbody>
          <tr><td>{"Distance (cm): "}</td><td>{ultrasonic}</td></tr>
          <tr><td>{"Temperature (C): "} </td><td>{temp}</td></tr>
          <tr><td>{"Humidity (%): "}</td><td>{humidity}</td></tr>
          <tr><td>{"Light (lumens): "}</td><td>{light}</td></tr>
        </tbody>
      </table>
    </div>
  );
}

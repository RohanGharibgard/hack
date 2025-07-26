import React, { useState } from 'react'
import { socket } from './App'

export default function SensorData() {
  const [ultrasonic, setUltrasonic] = useState("")
  const [temp, setTemp] = useState("")

  const [sensorData, setSensorData] = useState({
    ultrasonic: "",
    temp: "",
    humidity: "",
    light: ""
  });

  socket.on('ultrasonic', (data) => {
    setSensorData({
      ultrasonic: data,
      ...sensorData
    })
  })

  socket.on('temp', (data) => {
    setSensorData({
      temp: data,
      ...sensorData
    })
  })

  socket.on('humidity', (data) => {
    setSensorData({
      humidity: data,
      ...sensorData
    })
  })

  socket.on('light', (data) => {
    setSensorData({
      light: data,
      ...sensorData
    })
  })




  return (
    <div>
      <table style={{textAlign: 'left'}}>
        <tr><td>Ultrasonic: </td><td>{ultrasonic}</td></tr>
        <tr><td>Temperature: </td><td>{ultrasonic}</td></tr>
        <tr><td>Humidity: </td><td>{ultrasonic}</td></tr>
        <tr><td>Light: </td><td>{ultrasonic}</td></tr>
      </table>
    </div>
  );
}

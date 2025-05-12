import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Login     from './pages/Login'
import Dashboard from './pages/Dashboard'
import Listings  from './pages/Listings'

export default function App() {
  return (
    <Routes>
      <Route path="/"          element={<Login    />} />
      <Route path="/dashboard" element={<Dashboard/>} />
      <Route path="/listings"  element={<Listings />} />
    </Routes>
  )
}

// src/pages/MapView.tsx
import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

export default function MapView() {
  const [zip, setZip] = useState('')
  const [selectedZip, setSelectedZip] = useState('')
  const navigate = useNavigate()

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    setSelectedZip(zip.trim())
  }

  const mapUrl = selectedZip
    ? `https://maps.google.com/maps?q=${selectedZip}&z=12&output=embed`
    : ''

  return (
    <div style={{ padding: 24, maxWidth: 800, margin: '0 auto' }}>
      {/* Back Button */}
      <button
        onClick={() => navigate('/dashboard')}
        style={{
          padding: '8px 16px',
          marginBottom: 16,
          border: 'none',
          borderRadius: 4,
          backgroundColor: '#3182ce',
          color: 'white',
          cursor: 'pointer',
          fontSize: 14,
        }}
      >
        Back to Dashboard
      </button>

      <h1 style={{ fontSize: 24, marginBottom: 16 }}>Map View</h1>

      <form onSubmit={handleSubmit} style={{ marginBottom: 16 }}>
        <input
          type="text"
          placeholder="Enter ZIP code"
          value={zip}
          onChange={e => setZip(e.target.value)}
          style={{
            padding: '8px',
            fontSize: 14,
            width: 200,
            marginRight: 8,
            boxSizing: 'border-box',
          }}
        />
        <button
          type="submit"
          style={{
            padding: '8px 16px',
            fontSize: 14,
            cursor: 'pointer',
          }}
        >
          Show Map
        </button>
      </form>

      {selectedZip && (
        <div
          style={{
            width: '100%',
            height: 500,
            border: '1px solid #ccc',
            borderRadius: 4,
            overflow: 'hidden',
          }}
        >
          <iframe
            title="map"
            src={mapUrl}
            style={{ width: '100%', height: '100%', border: 0 }}
            allowFullScreen
            loading="lazy"
          />
        </div>
      )}
    </div>
  )
}

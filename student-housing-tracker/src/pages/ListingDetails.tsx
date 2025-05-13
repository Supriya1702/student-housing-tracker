// src/pages/ListingDetails.tsx
import React from 'react'
import { useLocation, useParams, useNavigate } from 'react-router-dom'

interface Listing {
  id: string
  title: string
  price: number
  location: string
  imageUrl: string
  buildingType: string
  petFriendly: boolean
}

export default function ListingDetails() {
  const { id } = useParams<{ id: string }>()
  const locationState = useLocation().state as Listing | undefined
  const navigate = useNavigate()

  if (!locationState || locationState.id !== id) {
    return (
      <div style={{ padding: 24, textAlign: 'center' }}>
        <p>Listing not found.</p>
        <button
          onClick={() => navigate('/listings')}
          style={{ padding: '8px 16px', marginTop: 16 }}
        >
          Back to Listings
        </button>
      </div>
    )
  }

  const { title, price, location, imageUrl, buildingType, petFriendly } = locationState

  return (
    <div style={{ padding: 24, maxWidth: 600, margin: '0 auto' }}>
      <button
        onClick={() => navigate('/listings')}
        style={{ marginBottom: 16, padding: '8px 16px', cursor: 'pointer' }}
      >
        Back to Listings
      </button>

      <div style={{ border: '1px solid #e2e8f0', borderRadius: 8, overflow: 'hidden', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' }}>
        <div style={{ height: 300, overflow: 'hidden' }}>
          <img src={imageUrl} alt={title} style={{ width: '100%', height: '100%', objectFit: 'cover' }}/>
        </div>
        <div style={{ padding: 24 }}>
          <h1 style={{ fontSize: 24, marginBottom: 8 }}>{title}</h1>
          <p style={{ marginBottom: 8 }}><strong>Price:</strong> ${price}</p>
          <p style={{ marginBottom: 8 }}><strong>Location:</strong> {location}</p>
          <p style={{ marginBottom: 8 }}><strong>Building Type:</strong> {buildingType}</p>
          <p><strong>Pet Friendly:</strong> {petFriendly ? 'Yes' : 'No'}</p>
        </div>
      </div>
    </div>
  )
}

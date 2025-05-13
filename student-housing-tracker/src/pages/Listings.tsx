// src/pages/Listings.tsx
import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'

interface Listing {
  id: string
  title: string
  price: number
  location: string
  zip: string
  imageUrl: string
  buildingType: string
  petFriendly: boolean
}

const initialListings: Listing[] = [
  {
    id: '1',
    title: 'Sunny 2-bed near campus',
    price: 1200,
    location: 'Amherst',
    zip: '01002',
    imageUrl: 'https://picsum.photos/seed/l1/400/300',
    buildingType: 'apartment',
    petFriendly: true,
  },
  {
    id: '2',
    title: 'Cozy studio downtown',
    price: 900,
    location: 'North Amherst',
    zip: '01002',
    imageUrl: 'https://picsum.photos/seed/l2/400/300',
    buildingType: 'house',
    petFriendly: false,
  },
  {
    id: '3',
    title: 'Spacious house share',
    price: 700,
    location: 'Hadley',
    zip: '01035',
    imageUrl: 'https://picsum.photos/seed/l3/400/300',
    buildingType: 'townhouse',
    petFriendly: true,
  },
]

const styles: { [key: string]: React.CSSProperties } = {
  container:    { padding: 24, maxWidth: 1200, margin: '0 auto' },
  header:       { display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24 },
  buttonGroup:  { display: 'flex', gap: 8 },
  button:       { padding: '8px 16px', border: 'none', borderRadius: 4, cursor: 'pointer', fontSize: 14 },
  btnPrimary:   { backgroundColor: '#3182ce', color: 'white' },
  btnSecondary: { backgroundColor: '#4a5568', color: 'white' },
  grid:         { display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 16 },
  card:         { border: '1px solid #e2e8f0', borderRadius: 8, overflow: 'hidden', backgroundColor: 'white', display: 'flex', flexDirection: 'column', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' },
  imgContainer: { height: 200, overflow: 'hidden' },
  image:        { width: '100%', height: '100%', objectFit: 'cover' as const },
  cardContent:  { padding: 16, flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' },
  title:        { fontSize: 18, fontWeight: 600, marginBottom: 8 },
  location:     { fontSize: 14, color: '#718096', marginBottom: 12 },
  price:        { fontSize: 16, fontWeight: 700 },
}

export default function Listings() {
  const [listings, setListings] = useState<Listing[]>([])
  const [loading,  setLoading]  = useState(true)
  const [error,    setError]    = useState<string | null>(null)
  const navigate = useNavigate()

  useEffect(() => {
    setTimeout(() => {
      setListings(initialListings)
      setLoading(false)
    }, 300)
  }, [])

  if (loading) return <p style={{ textAlign: 'center' }}>Loading…</p>
  if (error)   return <p style={{ textAlign: 'center', color: 'red' }}>{error}</p>

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1 style={{ fontSize: 24 }}>All Listings</h1>
        <div style={styles.buttonGroup}>
          <button onClick={() => navigate('/dashboard')} style={{ ...styles.button, ...styles.btnSecondary }}>
            Back to Dashboard
          </button>
          <button onClick={() => navigate('/map')} style={{ ...styles.button, ...styles.btnSecondary }}>
            Map View
          </button>
          <button onClick={() => navigate('/')} style={{ ...styles.button, ...styles.btnSecondary }}>
            Logout
          </button>
        </div>
      </header>

      <div style={styles.grid}>
        {listings.map(l => (
          <div
            key={l.id}
            style={styles.card}
            onClick={() => navigate(`/listings/${l.id}`, { state: l })}
          >
            <div style={styles.imgContainer}>
              <img src={l.imageUrl} alt={l.title} style={styles.image} />
            </div>
            <div style={styles.cardContent}>
              <div>
                <div style={styles.title}>{l.title}</div>
                <div style={styles.location}>📍 {l.location}</div>
              </div>
              <div style={styles.price}>${l.price}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

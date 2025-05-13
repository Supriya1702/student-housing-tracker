// src/pages/Dashboard.tsx
import React from 'react'
import { useNavigate } from 'react-router-dom'

interface Listing {
  id: string
  title: string
  price: number
  location: string
  imageUrl: string
}

const recentlyVisited: Listing[] = [
  {
    id: 'rv1',
    title: 'Cozy 2-bed near Quabbin',
    price: 1100,
    location: 'Amherst',
    imageUrl: 'https://picsum.photos/seed/rv1/400/300',
  },
  {
    id: 'rv2',
    title: 'Modern studio',
    price: 950,
    location: 'North Amherst',
    imageUrl: 'https://picsum.photos/seed/rv2/400/300',
  },
  {
    id: 'rv3',
    title: 'Spacious quad',
    price: 800,
    location: 'Hadley',
    imageUrl: 'https://picsum.photos/seed/rv3/400/300',
  },
]

const recommended: Listing[] = [
  {
    id: 'rc1',
    title: 'Sunny loft',
    price: 1250,
    location: 'Amherst',
    imageUrl: 'https://picsum.photos/seed/rc1/400/300',
  },
  {
    id: 'rc2',
    title: 'Quiet basement apt',
    price: 700,
    location: 'South Amherst',
    imageUrl: 'https://picsum.photos/seed/rc2/400/300',
  },
  {
    id: 'rc3',
    title: 'Charming cottage',
    price: 1400,
    location: 'Hadley',
    imageUrl: 'https://picsum.photos/seed/rc3/400/300',
  },
]

const styles: { [k: string]: React.CSSProperties } = {
  container: { padding: 24, maxWidth: 1200, margin: '0 auto' },
  header: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 32 },
  title: { fontSize: 28, fontWeight: 700 },
  buttonGroup: { display: 'flex', gap: 8 },
  button: { padding: '8px 16px', border: 'none', borderRadius: 4, cursor: 'pointer', fontSize: 14 },
  btnPrimary: { backgroundColor: '#3182ce', color: 'white' },
  btnSuccess: { backgroundColor: '#38a169', color: 'white' },
  btnDanger: { backgroundColor: '#e53e3e', color: 'white' },
  section: { marginBottom: 48 },
  sectionTitle: { fontSize: 22, fontWeight: 600, marginBottom: 16 },
  grid: { display: 'grid', gridTemplateColumns: 'repeat(3,1fr)', gap: 16 },
  card: { backgroundColor: 'white', border: '1px solid #e2e8f0', borderRadius: 8, overflow: 'hidden', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', display: 'flex', flexDirection: 'column', cursor: 'pointer' },
  imgContainer: { height: 160, overflow: 'hidden' },
  image: { width: '100%', height: '100%', objectFit: 'cover' as const },
  cardContent: { padding: 16, flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' },
  cardTitle: { fontSize: 18, fontWeight: 600, marginBottom: 8 },
  cardLocation: { fontSize: 14, color: '#718096', marginBottom: 12 },
  cardPrice: { fontSize: 16, fontWeight: 700 },
}

export default function Dashboard() {
  const navigate = useNavigate()
  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <div style={styles.title}>Dashboard</div>
        <div style={styles.buttonGroup}>
          <button onClick={() => navigate('/listings')} style={{ ...styles.button, ...styles.btnPrimary }}>
            View Listings
          </button>
          <button onClick={() => navigate('/map')} style={{ ...styles.button, ...styles.btnSuccess }}>
            Map View
          </button>
          <button onClick={() => navigate('/')} style={{ ...styles.button, ...styles.btnDanger }}>
            Logout
          </button>
        </div>
      </header>

      <section style={styles.section}>
        <div style={styles.sectionTitle}>Recently Visited</div>
        <div style={styles.grid}>
          {recentlyVisited.map(l => (
            <div key={l.id} style={styles.card} onClick={() => navigate(`/listings/${l.id}`, { state: l })}>
              <div style={styles.imgContainer}>
                <img src={l.imageUrl} alt={l.title} style={styles.image} />
              </div>
              <div style={styles.cardContent}>
                <div>
                  <div style={styles.cardTitle}>{l.title}</div>
                  <div style={styles.cardLocation}>📍 {l.location}</div>
                </div>
                <div style={styles.cardPrice}>${l.price}</div>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section>
        <div style={styles.sectionTitle}>Listings for You</div>
        <div style={styles.grid}>
          {recommended.map(l => (
            <div key={l.id} style={styles.card} onClick={() => navigate(`/listings/${l.id}`, { state: l })}>
              <div style={styles.imgContainer}>
                <img src={l.imageUrl} alt={l.title} style={styles.image} />
              </div>
              <div style={styles.cardContent}>
                <div>
                  <div style={styles.cardTitle}>{l.title}</div>
                  <div style={styles.cardLocation}>📍 {l.location}</div>
                </div>
                <div style={styles.cardPrice}>${l.price}</div>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}

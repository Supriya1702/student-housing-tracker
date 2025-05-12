import React, { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'

interface Listing {
  id: string
  title: string
  price: number
  location: string
}

const mockListings: Listing[] = [
  { id: '1', title: 'Sunny 2-bed near campus', price: 1200, location: 'Amherst' },
  { id: '2', title: 'Cozy studio downtown',  price: 900,  location: 'North Amherst' },
  { id: '3', title: 'Spacious house share', price: 700,  location: 'Hadley' },
]

export default function Dashboard() {
  const [listings, setListings] = useState<Listing[]>([])
  const [loading,  setLoading]  = useState(true)
  const navigate = useNavigate()

  useEffect(() => {
    setTimeout(() => {
      setListings(mockListings)
      setLoading(false)
    }, 300)
  }, [])

  if (loading) return <p className="p-4 text-center">Loading…</p>

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <header className="flex items-center justify-between mb-8">
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <div className="space-x-4">
          <Link to="/listings"
                className="px-4 py-2 bg-green-600 text-white rounded">
            View All Listings
          </Link>
          <button onClick={() => navigate('/')}
                  className="px-4 py-2 bg-red-600 text-white rounded">
            Logout
          </button>
        </div>
      </header>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {listings.map(l => (
          <div key={l.id}
               className="border rounded-lg p-4 shadow-sm hover:shadow-md">
            <h2 className="text-xl font-semibold mb-2">{l.title}</h2>
            <p className="text-sm mb-1">📍 {l.location}</p>
            <p className="text-lg font-bold">${l.price}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

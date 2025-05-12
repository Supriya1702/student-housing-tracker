// src/pages/Listings.tsx
import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'

interface Listing {
  id: string
  title: string
  price: number
  location: string
  imageUrl: string
}

type FormState = {
  title: string
  price: string
  location: string
  imageFile: File | null
  previewUrl: string
}

// Initial mock data
const initialListings: Listing[] = [
  {
    id: '1',
    title: 'Sunny 2-bed near campus',
    price: 1200,
    location: 'Amherst',
    imageUrl: 'https://via.placeholder.com/400x300?text=Sunny+2-bed',
  },
  {
    id: '2',
    title: 'Cozy studio downtown',
    price: 900,
    location: 'North Amherst',
    imageUrl: 'https://via.placeholder.com/400x300?text=Cozy+Studio',
  },
  {
    id: '3',
    title: 'Spacious house share',
    price: 700,
    location: 'Hadley',
    imageUrl: 'https://via.placeholder.com/400x300?text=House+Share',
  },
]

export default function Listings() {
  const [listings, setListings] = useState<Listing[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const [form, setForm] = useState<FormState>({
    title: '',
    price: '',
    location: '',
    imageFile: null,
    previewUrl: '',
  })
  const [showForm, setShowForm] = useState(false)

  const navigate = useNavigate()

  // Simulate fetching data on mount
  useEffect(() => {
    const simulateError = false
    new Promise<Listing[]>((resolve, reject) => {
      setTimeout(() => {
        if (simulateError) reject(new Error('Network error'))
        else resolve(initialListings)
      }, 300)
    })
      .then(data => setListings(data))
      .catch(err => {
        console.error(err)
        setError('Failed to load listings')
      })
      .finally(() => setLoading(false))
  }, [])

  // Text inputs handler
  const handleTextChange =
    (field: 'title' | 'price' | 'location') =>
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setForm(prev => ({ ...prev, [field]: e.target.value }))
    }

  // File input handler
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0] ?? null
    if (file) {
      const url = URL.createObjectURL(file)
      setForm(prev => ({ ...prev, imageFile: file, previewUrl: url }))
    }
  }

  // Submit handler
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    const newListing: Listing = {
      id: Date.now().toString(),
      title: form.title,
      price: Number(form.price),
      location: form.location,
      imageUrl: form.previewUrl || 'https://via.placeholder.com/400x300',
    }
    setListings(prev => [newListing, ...prev])
    setForm({ title: '', price: '', location: '', imageFile: null, previewUrl: '' })
    setShowForm(false)
  }

  if (loading) return <p className="p-4 text-center">Loading…</p>
  if (error) return <p className="p-4 text-center text-red-600">{error}</p>

  return (
    <div className="p-6 max-w-6xl mx-auto">
      {/* Header */}
      <header className="flex items-center justify-between mb-6">
        <h1 className="text-3xl font-bold">All Listings</h1>
        <div className="space-x-4">
          <button
            onClick={() => navigate('/dashboard')}
            className="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700"
          >
            Back to Dashboard
          </button>
          <button
            onClick={() => setShowForm(true)}
            className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Post a Listing
          </button>
        </div>
      </header>

      {/* Modal Form */}
      {showForm && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
            <h2 className="text-xl font-semibold mb-4 text-center">Post a Listing</h2>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block mb-1 font-medium">Title</label>
                <input
                  value={form.title}
                  onChange={handleTextChange('title')}
                  required
                  className="w-full px-3 py-2 border rounded focus:outline-none"
                />
              </div>
              <div>
                <label className="block mb-1 font-medium">Price</label>
                <input
                  type="number"
                  value={form.price}
                  onChange={handleTextChange('price')}
                  required
                  className="w-full px-3 py-2 border rounded focus:outline-none"
                />
              </div>
              <div>
                <label className="block mb-1 font-medium">Location</label>
                <input
                  value={form.location}
                  onChange={handleTextChange('location')}
                  required
                  className="w-full px-3 py-2 border rounded focus:outline-none"
                />
              </div>
              <div>
                <label className="block mb-1 font-medium">Image</label>
                <input
                  type="file"
                  accept="image/*"
                  onChange={handleFileChange}
                  className="w-full"
                />
                {form.previewUrl && (
                  <img
                    src={form.previewUrl}
                    alt="Preview"
                    className="mt-2 h-32 object-cover rounded"
                  />
                )}
              </div>
              <div className="flex justify-end space-x-2 pt-4">
                <button
                  type="button"
                  onClick={() => setShowForm(false)}
                  className="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
                >
                  Add Listing
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Listings Grid (3 columns on md+) */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {listings.map(l => (
          <div
            key={l.id}
            className="bg-white border rounded-lg overflow-hidden shadow-sm flex flex-col"
          >
            {/* Image area */}
            <div className="h-48 w-full overflow-hidden">
              <img
                src={l.imageUrl}
                alt={l.title}
                className="h-full w-full object-cover"
              />
            </div>
            {/* Content */}
            <div className="p-4 flex-1 flex flex-col justify-between">
              <div>
                <h2 className="text-xl font-semibold mb-1">{l.title}</h2>
                <p className="text-sm text-gray-600 mb-2">📍 {l.location}</p>
              </div>
              <p className="text-lg font-bold">${l.price}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

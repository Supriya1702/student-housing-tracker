import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function Login() {
  const navigate = useNavigate()

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    navigate('/dashboard')
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <form onSubmit={handleSubmit}
            className="bg-white p-6 rounded-lg shadow-md w-full max-w-sm">
        <h2 className="text-2xl font-semibold mb-6 text-center">Login</h2>
        <label htmlFor="email" className="block mb-2 text-sm">Email</label>
        <input id="email" type="email" required
               className="mb-4 w-full px-3 py-2 border rounded"/>
        <label htmlFor="password" className="block mb-2 text-sm">Password</label>
        <input id="password" type="password" required
               className="mb-6 w-full px-3 py-2 border rounded"/>
        <button type="submit"
                className="w-full py-2 bg-blue-600 text-white rounded">
          Sign In
        </button>
      </form>
    </div>
  )
}

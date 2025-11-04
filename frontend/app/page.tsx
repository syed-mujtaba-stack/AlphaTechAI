'use client'

import { useState } from 'react'
import axios from 'axios'

export default function Home() {
  const [formula, setFormula] = useState('CD:[2015-07-01 TO 2015-07-05] AND EN:INDIVIDUAL OW:USA')
  const [spreadsheetUrl, setSpreadsheetUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const [status, setStatus] = useState('')
  const [error, setError] = useState('')
  const [results, setResults] = useState<any>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    setStatus('Starting extraction...')
    setResults(null)

    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
      
      setStatus('Scraping USPTO data with AI...')
      const response = await axios.post(`${apiUrl.replace(/\/$/, '')}/api/scrape`, {
        formula,
        spreadsheet_url: spreadsheetUrl
      }, {
        timeout: 300000
      })

      if (response.data.success) {
        setStatus(`✓ Successfully extracted ${response.data.count} trademarks!`)
        setResults(response.data)
      } else {
        setError(response.data.message || 'Failed to extract data')
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || err.message || 'An error occurred')
      setStatus('')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-12">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-12">
            <div className="flex items-center justify-center mb-6">
              <img 
                src="/logo.png" 
                alt="AlphaTechAI Logo" 
                className="h-16 mr-4"
                onError={(e) => {
                  e.currentTarget.style.display = 'none';
                }}
              />
              <h1 className="text-4xl font-bold text-gray-900">
                AlphaTechAI
              </h1>
            </div>
            <h2 className="text-3xl font-semibold text-gray-800 mb-4">
              USPTO Trademark Scraper
            </h2>
            <p className="text-lg text-gray-600">
              AI-powered automation to extract cancelled trademark data and save to Google Sheets
            </p>
          </div>

          <div className="bg-white rounded-lg shadow-lg p-8">
            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  USPTO Search Formula
                </label>
                <textarea
                  value={formula}
                  onChange={(e) => setFormula(e.target.value)}
                  rows={3}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                  placeholder="CD:[2015-07-01 TO 2015-07-05] AND EN:INDIVIDUAL OW:USA"
                  required
                />
                <p className="mt-2 text-sm text-gray-500">
                  Example: CD:[2015-07-01 TO 2015-07-05] AND EN:INDIVIDUAL OW:USA
                </p>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Google Sheets URL
                </label>
                <input
                  type="url"
                  value={spreadsheetUrl}
                  onChange={(e) => setSpreadsheetUrl(e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                  placeholder="https://docs.google.com/spreadsheets/d/..."
                  required
                />
                <p className="mt-2 text-sm text-gray-500">
                  Make sure the spreadsheet is shared with the service account
                </p>
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-3 px-6 rounded-lg transition duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? 'Extracting Data...' : 'Start Extraction'}
              </button>
            </form>

            {loading && (
              <div className="mt-6 p-4 bg-blue-50 rounded-lg">
                <div className="flex items-center">
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-indigo-600 mr-3"></div>
                  <p className="text-indigo-700">{status}</p>
                </div>
              </div>
            )}

            {error && (
              <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg">
                <p className="text-red-700">Error: {error}</p>
              </div>
            )}

            {results && !loading && (
              <div className="mt-6 p-6 bg-green-50 border border-green-200 rounded-lg">
                <h3 className="text-lg font-semibold text-green-800 mb-2">
                  {status}
                </h3>
                <p className="text-green-700">
                  Data has been successfully written to your Google Sheet
                </p>
                {results.data && results.data.length > 0 && (
                  <div className="mt-4">
                    <p className="text-sm text-gray-600 mb-2">Preview of extracted data:</p>
                    <div className="bg-white rounded border border-gray-200 p-3 max-h-64 overflow-auto">
                      <pre className="text-xs">{JSON.stringify(results.data.slice(0, 3), null, 2)}</pre>
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>

          <div className="mt-8 bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">How it works</h2>
            <ol className="list-decimal list-inside space-y-2 text-gray-700">
              <li>Enter your USPTO search formula (e.g., date range and filters)</li>
              <li>Provide your Google Sheets URL</li>
              <li>Click "Start Extraction" and let AI do the work</li>
              <li>Data is automatically extracted and saved to your spreadsheet</li>
            </ol>
            
            <div className="mt-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
              <h3 className="font-semibold text-yellow-800 mb-2">Extracted Fields:</h3>
              <ul className="list-disc list-inside text-yellow-700 text-sm">
                <li>Correspondent Email</li>
                <li>Phone Number</li>
                <li>Correspondent Name</li>
                <li>Date Cancelled</li>
                <li>US Serial Number</li>
                <li>Mark (Trademark Name)</li>
                <li>Goods & Services Description</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

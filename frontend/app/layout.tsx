import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'AlphaTechAI - USPTO Trademark Scraper',
  description: 'AI-powered automated USPTO trademark data extraction to Google Sheets by AlphaTechAI',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}

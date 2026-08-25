import { useState } from 'react'
// import './App.css'

export default function App() {
  const [count, setCount] = useState(0)

  return (
    <main className="app">
      <p className="eyebrow">Vite + React + TypeScript</p>
      <h1>Front</h1>
      <p className="intro">A small, typed starting point for the frontend.</p>
      <button type="button" onClick={() => setCount((current) => current + 1)}>
        Count is {count}
      </button>
    </main>
  )
}

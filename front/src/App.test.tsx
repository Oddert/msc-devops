import { fireEvent, render, screen } from '@testing-library/react'
import App from './App'

describe('App', () => {
  it('increments the counter', () => {
    render(<App />)

    fireEvent.click(screen.getByRole('button', { name: 'Count is 0' }))

    expect(screen.getByRole('button', { name: 'Count is 1' })).toBeInTheDocument()
  })
})

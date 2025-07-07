
export async function searchDocuments(payload) {
  const res = await fetch('http://localhost:8000/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  })

  if (!res.ok) throw new Error('Search failed')
  return await res.json()
}

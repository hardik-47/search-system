<!-- layouts/default.vue -->
<template>
  <div class="min-h-screen bg-gray-50 text-gray-900">
    <header class="bg-white shadow">
      <div class="container mx-auto px-4 py-4 flex justify-between items-center">
        <h1 class="text-2xl font-bold text-blue-600">🧠 Tech Semantic Search</h1>
      </div>
    </header>
    <main class="container mx-auto px-4 py-6">
      <slot />
    </main>
  </div>
</template>

<!-- components/ResultCard.vue -->
<template>
  <div class="p-4 bg-white rounded shadow">
    <h2 class="text-xl font-semibold text-blue-700">{{ result.title }}</h2>
    <p class="text-sm text-gray-600 mb-2">
      📄 {{ result.type }} | 🗓️ {{ result.year }} | 📊 {{ result.citations }} citations
    </p>
    <p class="text-gray-800">
      {{ result.abstract }}
    </p>
  </div>
</template>

<script setup>
defineProps({
  result: Object
})
</script>

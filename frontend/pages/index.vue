
<template>
  <div>
    <SearchBar @search="handleSearch" />

    <div v-if="loading" class="mt-6 text-center text-gray-600">Searching...</div>

    <div v-if="results.length > 0" class="mt-6 space-y-4">
      <ResultCard
        v-for="doc in results"
        :key="doc.id"
        :result="doc"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import SearchBar from '../components/SearchBar.vue'
import ResultCard from '../components/ResultCard.vue'
import { searchDocuments } from '../utils/api'

const results = ref([])
const loading = ref(false)

const handleSearch = async (payload) => {
  loading.value = true
  const res = await searchDocuments(payload)
  results.value = res
  loading.value = false
}
</script>

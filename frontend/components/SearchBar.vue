
<template>
  <div class="bg-white p-4 rounded-xl shadow flex flex-col gap-4">
    <input
      v-model="query"
      type="text"
      placeholder="Enter your technical question..."
      class="border px-4 py-2 rounded w-full focus:outline-none focus:ring-2 focus:ring-blue-400"
    />

    <div class="flex items-center gap-4">
      <label>Type:</label>
      <select v-model="docType" class="border px-3 py-1 rounded">
        <option value="patents">Patents</option>
        <option value="papers">Papers</option>
      </select>
    </div>

    <button
      @click="onSearch"
      class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
    >
      🔍 Search
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const query = ref('')
const docType = ref('patents')

const emit = defineEmits(['search'])

const onSearch = () => {
  emit('search', { query: query.value, type: docType.value })
}
</script>

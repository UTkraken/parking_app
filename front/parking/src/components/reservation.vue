<template>
        <div v-if="loading">Loading...</div>
        <div v-else-if="error">Error: {{ error }}</div>
        <div v-else:"reservations" class="reservation-container">
          <h1>Reservations</h1>
          <table>
            <thead>
              <tr>
                  <th>Date</th>
                  <th>Parking</th>
                  <th>Floor</th>
                  <th>Spot</th>
                  <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="reservation in reservations" :key="reservation.id">
                  <td>{{ reservation.date }}</td>
                  <td>{{ reservation.parking.name }}</td>
                  <td>{{ reservation.floor.number }}</td>
                  <td>{{ reservation.spot.number }}</td>
                  <td>
                    <button v-on:click="editReservation(reservation.id)">Edit</button>
                    <button v-on:click="deleteReservation(reservation.id)">Delete</button>
                  </td>
              </tr>
            </tbody>
          </table>
        </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'

const toast = useToast() 

export default {
    name: "Reservation",
    methods: {
      editReservation(reservationId) {
        this.$router.push('new-reservation/'+ reservationId )
      },
      deleteReservation(reservationId) {
        axios.delete(`http://localhost:8000/api/reservations/${reservationId}`)
          .then(response => {
            this.reservations = this.reservations.filter(reservation => reservation.id !== reservationId)
            toast.success('Reservation deleted !')
          })
          .catch(error => {
            toast.error('Error during deleting reservation')
          })
      },
    },
    setup() {
      const reservations = ref([])
      const loading = ref(true)
      const error = ref(null)

      onMounted(async () => {
        try {
            const response = await fetch('http://localhost:8000/api/reservations')
            if (!response.ok) {
              throw new Error('Network response was not ok')
            }
            reservations.value = await response.json()
        } catch (err) {
            error.value = err.message
        } finally {
            loading.value = false
        }
      })

      return {
        reservations,
        loading,
        error,
      }
    }
}
</script>

<style scoped>
  .reservation-container {
    width: 100vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: 'Lato';
    color: #7D7D7D;
    margin-top: 10%;
  }

  h1 {
    font-size: 2em;
    font-weight: bolder;
    margin-bottom: 2%;
  }

  table {
    width: 80%;
    border-collapse: collapse;
    margin: 0 auto;
    table-layout: fixed;
  }

  thead, tbody {
    display: block;
    width: 100%;
  }

  thead tr, tbody tr {
    display: table;
    width: 100%;
    table-layout: fixed;
  }

  thead tr {
    font-size: 1.3em;
    font-weight: bold;
  }

  th, td {
    text-align: center;
    padding: 1rem;
    border-bottom: 1px solid #f19890;
    word-wrap: break-word;
  }

  th:nth-child(1), td:nth-child(1) { width: 20%; }
  th:nth-child(2), td:nth-child(2) { width: 20%; }
  th:nth-child(3), td:nth-child(3) { width: 15%; }
  th:nth-child(4), td:nth-child(4) { width: 15%; }
  th:nth-child(5), td:nth-child(5) { width: 30%; }

  tbody {
    max-height: 350px;
    overflow-y: auto;
  }

  button {
    margin: 20px auto;
    padding: 10px 20px;
    background-color: #FD8074;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-left: 2%;
  }

  button:hover {
    background-color: #f19890;
    transform: scale(0.95);
  }
</style>
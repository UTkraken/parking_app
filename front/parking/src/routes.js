import Home from './components/home.vue'
import Login from './components/login.vue'
import ReservationForm from './components/reservation-form.vue'
import Reservation from './components/reservation.vue'

export const routes = [
    {path: '/', component: Home},
    {path: '/login', component: Login},
    {path: '/reservation', component: Reservation},
    {path: '/new-reservation/:id?', component: ReservationForm},
]
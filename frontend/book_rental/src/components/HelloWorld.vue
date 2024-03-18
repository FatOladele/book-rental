<template>
  <v-container>
    <v-row>
      <v-col class="d-flex justify-end my-6">
        <v-btn class="mr-6 blue white--text" @click.stop="studentDialog = true">
          <v-icon class="mr-2">mdi-account-school</v-icon>
          <span >Add Student</span>
        </v-btn>
        <v-btn class="white blue--text" @click.stop="rentalDialog = true">
          <v-icon class="mr-2">mdi-book-plus-outline</v-icon>
          <span >Add Rental</span>
        </v-btn>
      </v-col>
    </v-row>
    <v-row class="d-flex justify-space-around">
      <v-col>
        <v-card 
          elevation="5"
          outlined
          tile
          class="d-flex flex-column"
          height="150px"
        >
          <v-row class="d-flex justify-center my-0">
            <v-col class="d-inline-flex justify-center">
              <v-icon x-large class="green--text mr-2">mdi-account-school</v-icon>
              <h1 class="align-self-center">{{totalStudent}}</h1>
            </v-col>
          </v-row>
          <v-row class="d-flex justify-center py-0 my-0">
            <v-col class="d-inline-flex justify-center py-0 my-0">
              <h4 class="0">Total Student</h4>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col>
        <v-card 
          elevation="5"
          outlined
          tile
          class="d-flex flex-column"
          height="150px"
        >
          <v-row class="d-flex justify-center my-0">
            <v-col class="d-inline-flex justify-center">
              <!-- <v-icon x-large class="green--text mr-2">mdi-account-school</v-icon> -->
              <h2 class="align-self-center">{{mostActiveStudent}}</h2>
            </v-col>
          </v-row>
          <v-row class="d-flex justify-center py-0 my-0">
            <v-col class="d-inline-flex justify-center py-0 my-0">
              <h4 class="0">Most Active Student</h4>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col>
        <v-card 
          elevation="5"
          outlined
          tile
          class="d-flex flex-column"
          height="150px"
        >
          <v-row class="d-flex justify-center my-0">
            <v-col class="d-inline-flex justify-center">
              <v-icon x-large class="green--text mr-2">mdi-book-outline</v-icon>
              <h1 class="align-self-center">{{totalRental}}</h1>
            </v-col>
          </v-row>
          <v-row class="d-flex justify-center py-0 my-0">
            <v-col class="d-inline-flex justify-center py-0 my-0">
              <h4 class="0">Total Rental</h4>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col>
        <v-card 
          elevation="5"
          outlined
          tile
          class="d-flex flex-column"
          height="150px"
        >
          <v-row class="d-flex justify-center my-0">
            <v-col class="d-inline-flex justify-center">
              <!-- <v-icon x-large class="green--text mr-2">mdi-book-outline</v-icon> -->
              <h2 class="align-self-center">{{mostRentedBook}}</h2>
            </v-col>
          </v-row>
          <v-row class="d-flex justify-center py-0 my-0">
            <v-col class="d-inline-flex justify-center py-0 my-0">
              <h4 class="0">Most Rented Book</h4>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-tabs v-model="tab">
          <v-tab
            v-for="item in items"
            :key="item.tab"
          >
            {{ item.text }}
          </v-tab>
        </v-tabs>
        <v-tabs-items v-model="tab">
          <v-tab-item v-for="i in items" :key="i.tab">
            <v-data-table
              :headers="tableHeader[i.header]"
              :items="tableData[i.data]"
              :items-per-page="10"
              class="elevation-1"
            >
            <template v-slot:[`item.actions`]="{ item }">
              <v-icon
                small
                class="mr-2"
                @click="editItem(i.tab, item)"
              >
                mdi-pencil
              </v-icon>
            </template>
          </v-data-table>
          </v-tab-item>
          <!-- <v-tab-item  key="rental" value="rental">
            <v-data-table
              :headers="rentalHeader"
              :items="rentalData"
              :items-per-page="10"
              class="elevation-1"
            ></v-data-table>
          </v-tab-item> -->
        </v-tabs-items>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-dialog
        v-model="studentDialog"
        persistent
        max-width="400"
      >
        <v-card>
          <v-card-title class="text-h5">
            Add new student
          </v-card-title>
          <v-card-text>
            <form>
              <v-text-field
                v-model="firstName"
                :error-messages="firstNameError"
                label="First Name"
                required
                @input="$v.firstName.$touch()"
                @blur="$v.firstName.$touch()"
              ></v-text-field>
              <v-text-field
                v-model="lastName"
                :error-messages="lastNameError"
                label="Last Name"
                required
                @input="$v.lastName.$touch()"
                @blur="$v.lastName.$touch()"
              ></v-text-field>
              <v-text-field
                v-model="studentId"
                :error-messages="studentIdError"
                label="Student ID"
                required
                @input="$v.studentId.$touch()"
                @blur="$v.studentId.$touch()"
              ></v-text-field>
              <v-row>
                <v-col class="d-flex justify-end">
                  <v-spacer></v-spacer>
                  <v-btn
                    color="green darken-1"
                    text
                    @click="submit"
                  >
                    Submit
                  </v-btn>
                  <v-btn
                    color="red darken-1"
                    text
                    @click="clear"
                  >
                    Clear
                  </v-btn>
                </v-col>
              </v-row>
            </form>
          </v-card-text>
        </v-card>
      </v-dialog> 
    </v-row>
    <v-row justify="center" >
      <v-col>
      <v-dialog
        v-model="rentalDialog"
        persistent
        max-width="400"
      >
        <v-card>
          <v-card-title class="text-h5">
            Add rental data
          </v-card-title>
          <v-card-text>
            <v-text-field
              label="Search book by title"
              append-icon="mdi-magnify"
              @click:append="fetchBooks"
              v-model="bookSearch"
            ></v-text-field>
            <form v-show="bookList.length > 0">
              <v-radio-group v-model="bookEditionKey" label="Select a book">
                <v-radio
                  v-for="book in bookList"
                  :key="book.value"
                  :label="book.text"
                  :value="book.value"
                ></v-radio>
              </v-radio-group>
              <v-select
                v-model="rentalStudentId"
                :items="rentalStudentItems"
                :error-messages="studentSelectErrors"
                item-text="text"
                item-value="value"
                label="Select a student"
                required
                @change="$v.rentalStudentId.$touch()"
                @blur="$v.rentalStudentId.$touch()"
              ></v-select>
              <v-menu
                v-model="returnDateMenu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="returnDate"
                    label="Return date"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="returnDate"
                  @input="returnDateMenu = false"
                ></v-date-picker>
              </v-menu>
              <v-row>
                <v-col class="d-flex justify-end">
                  <v-spacer></v-spacer>
                  <v-btn
                    color="green darken-1"
                    text
                    @click="rentalSubmit"
                  >
                    Submit
                  </v-btn>
                  <v-btn
                    color="red darken-1"
                    text
                    @click="rentalClear"
                  >
                    Clear
                  </v-btn>
                </v-col>
              </v-row>
            </form>
          </v-card-text>
        </v-card>
      </v-dialog>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-dialog
        v-model="editStudentDialog"
        persistent
        max-width="400"
      >
        <v-card>
          <v-card-title class="text-h5">
            Update student data
          </v-card-title>
          <v-card-text>
            <form>
              <v-text-field
                v-model="editedFirstName"
                :error-messages="editedFirstNameError"
                label="First Name"
                required
                @input="$v.editedFirstName.$touch()"
                @blur="$v.editedFirstName.$touch()"
              ></v-text-field>
              <v-text-field
                v-model="editedLastName"
                :error-messages="editedLastNameError"
                label="Last Name"
                required
                @input="$v.editedLastName.$touch()"
                @blur="$v.editedLastName.$touch()"
              ></v-text-field>
              <v-text-field
                v-model="editedStudentId"
                :error-messages="editedStudentIdError"
                label="Student ID"
                required
                @input="$v.editedStudentId.$touch()"
                @blur="$v.editedStudentId.$touch()"
              ></v-text-field>
              <v-row>
                <v-col class="d-flex justify-end">
                  <v-spacer></v-spacer>
                  <v-btn
                    color="green darken-1"
                    text
                    @click="updateStudentData"
                  >
                    Submit
                  </v-btn>
                  <v-btn
                    color="red darken-1"
                    text
                    @click="editStudentClear"
                  >
                    Clear
                  </v-btn>
                </v-col>
              </v-row>
            </form>
          </v-card-text>
        </v-card>
      </v-dialog> 
    </v-row>
    <v-row justify="center">
      <v-dialog
        v-model="editRentalDialog"
        persistent
        max-width="400"
      >
        <v-card>
          <v-card-title class="text-h5">
            Update return date
          </v-card-title>
          <v-card-text>
            <form>
              <v-menu
                v-model="editReturnDateMenu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="editedReturnDate"
                    label="Return date"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="editedReturnDate"
                  @input="editReturnDateMenu = false"
                ></v-date-picker>
              </v-menu>
              <v-row>
                <v-col class="d-flex justify-end">
                  <v-spacer></v-spacer>
                  <v-btn
                    color="green darken-1"
                    text
                    @click="updateRentalData"
                  >
                    Submit
                  </v-btn>
                  <v-btn
                    color="red darken-1"
                    text
                    @click="editRentalClear"
                  >
                    Clear
                  </v-btn>
                </v-col>
              </v-row>
            </form>
          </v-card-text>
        </v-card>
      </v-dialog> 
    </v-row>
    <v-snackbar
      :timeout="2000"
      v-model="snackbar"
      tile
      :color="snackbarColor"
    >
      {{snackbarText}}
    </v-snackbar>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import { validationMixin } from 'vuelidate'
  import { required } from 'vuelidate/lib/validators'
  export default {
    name: 'HelloWorld',
    mixins: [validationMixin],

    validations: {
      firstName: { required },
      lastName: { required },
      studentId: { required },
      editedFirstName: { required },
      editedLastName: { required },
      editedStudentId: { required },
      rentalStudentId: { required },
    },
    computed: {
      firstNameError () {
        const errors = []
        if (!this.$v.firstName.$dirty) return errors
        !this.$v.firstName.required && errors.push('First name is required')
        return errors
      },
      lastNameError () {
        const errors = []
        if (!this.$v.lastName.$dirty) return errors
        !this.$v.lastName.required && errors.push('Last name is required')
        return errors
      },
      studentIdError () {
        const errors = []
        if (!this.$v.studentId.$dirty) return errors
        !this.$v.studentId.required && errors.push('Student Id is required')
        return errors
      },
      editedFirstNameError () {
        const errors = []
        if (!this.$v.editedFirstName.$dirty) return errors
        !this.$v.editedFirstName.required && errors.push('First name is required')
        return errors
      },
      editedLastNameError () {
        const errors = []
        if (!this.$v.editedLastName.$dirty) return errors
        !this.$v.editedLastName.required && errors.push('Last name is required')
        return errors
      },
      editedStudentIdError () {
        const errors = []
        if (!this.$v.editedStudentId.$dirty) return errors
        !this.$v.editedStudentId.required && errors.push('Student Id is required')
        return errors
      },
      studentSelectErrors () {
        const errors = []
        if (!this.$v.rentalStudentId.$dirty) return errors
        !this.$v.rentalStudentId.required && errors.push('Student is required')
        return errors
      },
    },
    mounted () {
      this.fetchAnalytics()
      this.fetchStudents()
      this.fetchRentals()
    },
    data: () => ({
      tab: null,
      firstName: '',
      lastName: '',
      studentId: '',
      rentalStudentId: '',
      bookSearch: '',
      bookEditionKey: '',
      returnDate: (new Date()).toISOString().substr(0, 10),
      studentDialog: false,
      rentalDialog: false,
      returnDateMenu: false,
      editReturnDateMenu: false,
      tableHeader: {
        studentHeader: [
          { text: 'First Name', value: 'first_name' },
          { text: 'Last Name', value: 'last_name' },
          { text: 'Student ID', value: 'student_id' },
          { text: 'Actions', value: 'actions', sortable: false }
        ],
        rentalHeader: [
          { text: 'Student Name', value: 'student_name' },
          { text: 'Book Title', value: 'book_title' },
          { text: 'Date of Rental', value: 'rented_at' },
          { text: 'Date of Return', value: 'return_date' },
          { text: 'Charge', value: 'rental_charge' },
          { text: 'Status', value: 'status'},
          { text: 'Actions', value: 'actions', sortable: false }
        ],
      },      
      tableData: {
        studentData: [
          { id: 'ajgjd', first_name: 'Fatoki', last_name: 'Oladele', student_id: 'asddadasd' },
        ],
        rentalData: [
          { id: 'ajgjd', student_name: 'Fatoki', book_title: 'Oladele', rented_at: 'asddadasd', return_date: 'asddadasd', rental_charge: 200, status: 'active' },
        ],
      },
      rentalStudentItems: [],
      bookList: [],
      totalStudent: 0,
      mostActiveStudent: '',
      totalRental: 0,
      mostRentedBook: '',
      items: [
        { tab: 'student', header: 'studentHeader', data: 'studentData', text: 'Student'  },
        { tab: 'rental', header: 'rentalHeader', data: 'rentalData', text: 'Rental' },
      ],
      rentalStatusColor: {
        'active': 'green',
        'completed': 'blue',
      },
      editedFirstName: '',
      editedLastName: '',
      editedStudentId: '',
      editedStudentObjId: '',
      editedRentalObjId: '',
      editedReturnDate: (new Date()).toISOString().substr(0, 10),
      editStudentDialog: false,
      editRentalDialog: false,
      snackbar: false,
      snackbarColor: 'green',
      snackbarText: '',
    }),
    methods: {
      submit () {
        this.$v.$touch()
        this.addStudent()
        this.studentDialog = false
      },
      clear () {
        this.$v.$reset()
        this.firstName = ''
        this.lastName = ''
        this.studentId = ''
        this.studentDialog = false
      },
      rentalSubmit () {
        this.$v.$touch()
        this.addRental()
        this.rentalDialog = false
      },
      rentalClear () {
        this.$v.$reset()

        this.bookEditionKey = ''
        this.returnDate = (new Date()).toISOString().substr(0, 10)
        this.rentalStudentId = '',
        this.bookList = []
        this.bookSearch = ''
        this.rentalDialog = false
      },
      fetchStudents () {
        axios
          .get('http://localhost:8000/api/student')
          .then(response => {
            const studentData = response.data.data
            console.log(response.data)
            this.tableData.studentData = studentData
            this.rentalStudentItems = studentData.map(student => {
              return {
                text: `${student.first_name} ${student.last_name}, ${student.student_id}`,
                value: student.id,
              }
            })
          })
          .catch(error => {
            console.log(error)
          })
      },
      fetchRentals () {
        axios
          .get('http://localhost:8000/api/rental')
          .then(response => {
            const rentalData = response.data.data
            console.log(response.data)
            this.tableData.rentalData = rentalData.map(rental => {
              return { 
                id: rental.id, student_name: `${rental.student.first_name} ${rental.student.last_name}`, book_title: rental.book.book_title, rented_at: this.dateString(rental.rented_at), return_date: this.dateString(rental.return_date), rental_charge: rental.rental_charge, status: 'active' }
            })
          })
          .catch(error => {
            console.log(error)
          })
      },
      fetchAnalytics () {
        axios
          .get('http://localhost:8000/api/analytics')
          .then(response => {
            const { number_of_rentals, number_of_student, most_active_student, most_rented_book  } = response.data.data
            console.log(response.data)
            this.totalStudent = number_of_student
            this.mostActiveStudent = most_active_student
            this.totalRental = number_of_rentals
            this.mostRentedBook = most_rented_book
          })
          .catch(error => {
            console.log(error)
          })
      },
      fetchBooks () {
        const url = `http://localhost:8000/api/book?q=${this.bookSearch}`
        axios
          .get(url)
          .then(response => {
            const books = response.data.data.docs.filter((book) => book.number_of_pages_median)
            this.bookList = books.map(book => { return { text: `${book.title} (${book.number_of_pages_median} pages)`, value: book.cover_edition_key }})
          })
          .catch(error => {
            console.log(error)
          })
      },
      dateString(d) {
        const date = new Date(d)
        return date.toDateString()
      },
      rentalStatus(returnDate) {
        const date = new Date(returnDate)
        const today = new Date()
        return date > today ? 'active' : 'completed'
      },
      addStudent() {
        const requestData = {
          first_name: this.firstName,
          last_name: this.lastName,
          student_id: this.studentId,
        }
        axios
          .post('http://localhost:8000/api/student', requestData)
          .then(response => {
            console.log(response)
            this.fetchStudents()
            this.fetchAnalytics()
            this.showSnackbar(response.data.message, true)
          })
          .catch(error => {
            console.log(error)
            this.showSnackbar(error.data.message, false)
          })
        this.clear()
      },
      addRental() {
        const requestData = {
          edition_key: this.bookEditionKey,
          return_date: this.returnDate,
          student_id: this.rentalStudentId,
        }
        axios
          .post('http://localhost:8000/api/rental', requestData)
          .then(response => {
            console.log(response)
            this.fetchRentals()
            this.fetchAnalytics()
            this.showSnackbar(response.data.message, true)
          })
          .catch(error => {
            console.log(error)
            this.showSnackbar(error.response.data.message, false)
          })

        this.rentalClear()
      },
      editItem(tab, item) {
      console.log(tab, item)
        switch (tab) {
          case 'student':
            this.editStudentData(item)
            break;
          case 'rental':
            this.editRentalData(item)
            break;
          default:
            break;
        }

      },
      editStudentData(student) {
        this.editStudentDialog = true
        this.editedFirstName = student.first_name
        this.editedLastName = student.last_name
        this.editedStudentId = student.student_id
        this.editedStudentObjId = student.id
      },
      editRentalData(rental) {
        this.editRentalDialog = true
        this.editedRentalObjId = rental.id
        this.editedReturnDate = rental.return_date
      },
      editRentalClear() {
        this.editRentalDialog = false
        this.editedRentalObjId = ''
        this.editedReturnDate = (new Date()).toISOString().substr(0, 10)
      },
      editStudentClear() {
        this.editStudentDialog = false
        this.editedFirstName = ''
        this.editedLastName = ''
        this.editedStudentId = ''
        this.editedStudentObjId = ''
      },
      updateStudentData() {
        const requestData = {
          first_name: this.editedFirstName,
          last_name: this.editedLastName,
          student_id: this.editedStudentId,
        }
        const url = `http://localhost:8000/api/student/${this.editedStudentObjId}`
        axios
          .put(url, requestData)
          .then(response => {
            console.log(response)
            this.fetchStudents()
            this.editStudentClear()
            this.showSnackbar(response.data.message, true)
          })
          .catch(error => {
            console.log(error)
            this.showSnackbar(error.response.data.message, false)
          })
      },
      updateRentalData() {
        const url = `http://localhost:8000/api/rental/${this.editedRentalObjId}`
        axios
          .patch(url, { return_date: this.editedReturnDate})
          .then(response => {
            console.log(response)
            this.fetchRentals()
            this.editRentalClear()
            this.showSnackbar(response.data.message, true)
          })
          .catch(error => {
            console.log(error)
            this.showSnackbar(error.response.data.message, false)
          })
      },
      showSnackbar(msg, success = true) {
        this.snackbarColor = success? 'green' : 'red',
        this.snackbarText = msg
        this.snackbar = true
      }
    },
  }
</script>

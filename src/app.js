import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import './style.scss'

import EditCreate from './components/writings/EditCreate'
import WritingCreate from './components/writings/WritingCreate'
import WritingShow from './components/writings/WritingShow'
// import EditsShow from './components/writings/EditsShow'
import Login from './components/Auth/Login'
import Register from './components/Auth/Register'
import WriterProfile from './components/Auth/WriterProfile'
import OwnWritingShow from './components/Auth/OwnWritingShow'
import SearchIndex from './components/writings/SearchIndex'
import Nav from './components/common/Nav'




const App = () => {
  return (
    <BrowserRouter>
      <main>
        <div>
          <Nav />
          <Switch>
            {/* <Route path='/writings/:id/edits/edit:id' component={EditsShow} /> */}
            {/* <Route path='/writings/:id/edits' component={EditsShow} /> */}
            <Route path='/edit-orlogin' component={Login} />
            <Route path='/edit-writings/:id/edit' component={EditCreate} />
            <Route path='/edit-writings/:id/' component={WritingShow} />
            <Route path='/writingsubmit' component={WritingCreate} />
            <Route path='/register' component={Register} />
            <Route path='/writerprofile' component={WriterProfile} />
            <Route path='/writerprofile/:id/writings' component={OwnWritingShow} />

            <Route path='/writerlogin' component={Login} />

            <Route path='/edit-writings' component={SearchIndex} />


            <Route path='/edit-writings/:id/' component={WritingShow} />



          </Switch>
        </div>
      </main>
    </BrowserRouter>

  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)

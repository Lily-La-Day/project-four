import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import './style.scss'
import WritingsIndex from './components/writings/writingsIndex'
import EditCreate from './components/writings/EditCreate'
import WritingCreate from './components/writings/WritingCreate'
import WritingShow from './components/writings/WritingShow'
import EditsShow from './components/writings/EditsShow'
import Login from './components/Auth/Login'
import Register from './components/Auth/Register'
import Search from './components/writings/Search'
import Nav from './components/common/Nav'




const App = () => {
  return (
    <BrowserRouter>
      <main>
        <div>
          <Nav />
          <Switch>
            <Route path='/register' component={Register} />
            <Route path='/writerlogin' component={Login} />
            <Route path='/editorlogin' component={Login} />
            <Route path='/writings/search' component={Search} />
            <Route path='/writings/:id/edits' component={EditsShow} />
            <Route path='/writings/:id/edit' component={EditCreate} />
            <Route path='/writings/:id/' component={WritingShow} />

            <Route path='/writingsubmit' component={WritingCreate} />
            <WritingsIndex />
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

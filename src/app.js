import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import './style.scss'
import WritingsIndex from './components/writings/writingsIndex'
import EditCreate from './components/writings/EditCreate'
import WritingCreate from './components/writings/WritingCreate'
// import WritingShow from './components/writings/WritingShow'
import Login from './components/Auth/Login'





const App = () => {
  return (
    <BrowserRouter>
      <main>
        <div>
          <Switch>
            <Route path='/login' component={Login} />
            {/* <Route path='/writings/:id/' component={WritingShow} /> */}
            <Route path='/writings/:id/edit' component={EditCreate} />
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

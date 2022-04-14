import React from 'react'
import { Route, Routes } from 'react-router-dom'
import { appRoutes } from '../router'

function AppRouter() {
  return (
    <Routes>
        {appRoutes.map(route =>
            <Route
                key={route.path}
                path={route.path} 
                element={route.element} 
                exact={route.exact} 
            />
        )}
    </Routes>
  )
}

export default AppRouter
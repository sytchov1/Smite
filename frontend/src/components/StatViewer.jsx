import React, { useState, useEffect } from 'react'
import StatList from './StatList'
import CustomSelect from './UI/select/customSelect'
import { STATS } from '../values/stats.js'

function StatViewer() {
  const [category, setCategory] = useState('Защита')
  const [stats, setStats] = useState([])
  const options = STATS.map(s => Object.create( null, {
    value: {
      value: s['name']
    },
    label: {
      value: s['name']
    }
  }))

  useEffect(() => {
    setStats(STATS.find(obj => obj.name === category)['substats'].map(stat => Object.create(null, {
      name: {
        value: stat
      },
      value: {
        value: 0
      },
    })))
  }, [category])

  const handleChange = (e) => {
    setCategory(e.value)
  }

  return (
    <div className='StatViewer'>
        <CustomSelect options={options} value={category} onChange={handleChange}/>
        <StatList stats={stats}/>
    </div>
  )
}

export default StatViewer
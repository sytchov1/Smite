import React, { useState } from 'react'
import Equipment from '../components/Equipment'
import StatViewer from '../components/StatViewer'

function Character() {
  const [eqip, setEqip] = useState([
    {slot: 'Голова', value: null},
    {slot: 'Шея', value: null},
    {slot: 'Плечи', value: null},
    {slot: 'Спина', value: null},
    {slot: 'Грудь', value: null},
    {slot: 'Рубашка', value: null},
    {slot: 'Гербовая накидка', value: null},
    {slot: 'Запястья', value: null},
    {slot: 'Правая рука', value: null},
    {slot: 'Левая рука', value: null},
    {slot: 'Кисти рук', value: null},
    {slot: 'Пояс', value: null},
    {slot: 'Ноги', value: null},
    {slot: 'Ступни', value: null},
    {slot: 'Палец 1', value: null},
    {slot: 'Палец 2', value: null},
    {slot: 'Аксессуар 1', value: null},
    {slot: 'Аксессуар 2', value: null},
    {slot: 'Дальний бой', value: null},
  ]);

  return (
    <div>
      <div className='character-info'>
        <div className='class-icon' style={{backgroundImage: `url('https://wow.zamimg.com/images/wow/icons/large/classicon_priest.jpg')`}}></div>
        <span className='character-name'>Имя персонажа</span>
      </div>
      <Equipment eqip={eqip} setEqip={setEqip}/>
      <div className='stats'>
        <StatViewer/>
      </div>
    </div>
  )
}

export default Character
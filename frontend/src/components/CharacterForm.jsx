import React, { useEffect, useState } from 'react'
import Input from './UI/input/Input'
import Button from './UI/button/Button'
import ClassList from './ClassList'
import Loader from './UI/loader/Loader'
import { useFetching } from '../hooks/useFetching';
import { Service } from '../API/Service';

function CharacterForm() {
  const [classes, setClasses] = useState([]);
  const [fetchClasses, isLoading, classesError] = useFetching(async () => {
    const response = await Service.getClasses();
    setClasses([...response.data])
  })

  useEffect(() => {
    fetchClasses();
  }, [])

  return (
    <div className='CharacterForm'>
      <div>Новый персонаж</div>
      <Input placeholder='Имя'/>
      {classesError &&
        <h1>Произошла ошибка {classesError}</h1>
      }
      <ClassList cls={classes}/>
      {isLoading &&
        <div style={{display: 'flex', justifyContent: 'center', marginTop: '50px'}}><Loader></Loader></div>
      }
      <Button onClick={() => console.log(classes)}>Создать</Button>
    </div>
  )
}

export default CharacterForm
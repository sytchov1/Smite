import Character from '../pages/Character';
import Characters from '../pages/Characters';
import Simulation from '../pages/Simulation';
import NewCharacter from '../pages/NewCharacter';

export const appRoutes = [
    {path: '/', element: <Characters/>, exact: false},
    {path: '/characters', element: <Characters/>, exact: true},
    {path: '/characters/:id', element: <Character/>, exact: true},
    {path: '/characters/new', element: <NewCharacter/>, exact: true},
    {path: '/simulation', element: <Simulation/>, exact: false},
]
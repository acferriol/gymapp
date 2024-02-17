import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";
import { PURGE } from "redux-persist";

export const loginUser = createAsyncThunk(
    'user/loginUser',
    async ( userCredentials )=>{
        const request = await axios.post(`../../usuarios.json`,userCredentials)
        const response = await request.data;
        console.log(response);
        localStorage.setItem('user', JSON.stringify(response));
        return response ;
    }
);

const userSlice = createSlice({
    name: 'user',
    initialState:{
        user: null,
        isLogin: false,
        error: null,
    },
    reducers:{
        resetUserState: (state) => {
            state.user = null;
            state.isLogin = false;
            state.error = null;
        },
    },
    extraReducers:(builder)=>{
        builder
        .addCase(loginUser.fulfilled,(state,action)=>{
            state.isLogin = true ;
            state.user = action.payload;
            state.error = null ;
        })
        .addCase(loginUser.rejected,(state,action)=>{
            state.isLogin = false ;
            state.user = null;
            console.log(action.error.message);
            if(action.error.message === 'Request failed with status code 401'){
                state.error = true
            }else{
                state.error = action.error.message;
                //arreglar aki para q muestre bien los errores
            }
        
        })
        .addCase(PURGE, (state) => {
            customEntityAdapter.removeAll(state);
        });
    }
});
export const { resetUserState } = userSlice.actions ;
export default userSlice.reducer ;


//arreglar esto que la persistencia se queda , y a veces cuando se recarga sale , ver como arreglar eso
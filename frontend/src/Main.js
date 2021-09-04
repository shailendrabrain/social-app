import React from 'react';
import {Route, Switch} from "react-router-dom";
import Login from "./components/authentication/Login";
import Signup from "./components/authentication/Signup";
import Home from "./components/home/Home";
import NotFound from "./components/authentication/NotFound";
import Header from "./components/layout/Header";

const Main = () => {
    return (
        <div>
            <Header/>
            <Switch>
                <Route exact path="/login/" component={Login}/>
                <Route exact path="/signup/" component={Signup}/>
                <Route exact path="/" component={Home}/>
                <Route componetn={NotFound}/>
            </Switch>
        </div>
    );
};

export default Main;
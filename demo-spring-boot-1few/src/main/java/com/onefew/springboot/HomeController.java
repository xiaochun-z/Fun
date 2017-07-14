package com.onefew.springboot;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * Created by caden on 2017/7/14.
 */
@Controller
@RequestMapping("/")
public class HomeController {

    @Autowired
    UserDao userDao;

    @GetMapping("/")
    public String index(Model model){
        model.addAttribute("name","world");
        return "home";
    }

    @GetMapping("/{id}")
    public String findById(Model model, @PathVariable(value = "id") int id){
        User u = userDao.findById(id);
        model.addAttribute("name",u.getName());
        return "home";
    }
}

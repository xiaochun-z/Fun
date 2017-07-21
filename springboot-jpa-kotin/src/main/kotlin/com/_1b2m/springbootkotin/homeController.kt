package com._1b2m.springbootkotin

import com.sun.org.apache.xpath.internal.operations.Mod
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Controller
import org.springframework.ui.Model
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RequestMapping

@Controller
@RequestMapping("/")
class homeController {
    @Autowired
    lateinit var repository: UserRepository

    @RequestMapping("/")
    fun index(model: Model): String {
        val users = repository.findAll().toList()
        return setModel(model, users)
    }

    @RequestMapping("/add/{id}/{firstName}/{lastName}")
    fun add(model: Model, @PathVariable("id") id: Long, @PathVariable("firstName") firstName: String, @PathVariable("lastName") lastName: String): String {
        repository.save(User(id, firstName, lastName))
        model.addAttribute("id", id)
        return "add"
    }

    @GetMapping("/get/id/{id}")
    fun getbyId(model: Model, @PathVariable("id") id: Long): String {
        val user = repository.findOne(id)
        model.addAttribute("user", user)
        return "view"
    }

    @GetMapping("/get/name/{lastName}")
    fun getByLastName(model: Model, @PathVariable("lastName") lastName: String): String {
        val users = repository.findByLastName(lastName)
        return setModel(model, users)
    }

    @GetMapping("/get/{name}")
    fun getByName(model: Model, @PathVariable("name") name: String): String {
        val users = repository.findUser(name)
        return setModel(model, users)
    }

    private fun setModel(model: Model, users: List<User>): String {
        model.addAttribute("users", users)
        return "list"
    }
}
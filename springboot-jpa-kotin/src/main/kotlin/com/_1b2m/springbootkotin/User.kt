package com._1b2m.springbootkotin

import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.GenerationType
import javax.persistence.Id

@Entity
data class User(@Id @GeneratedValue(strategy = GenerationType.AUTO) val id: Long = 0L, val firstName: String = "", val lastName: String = "")
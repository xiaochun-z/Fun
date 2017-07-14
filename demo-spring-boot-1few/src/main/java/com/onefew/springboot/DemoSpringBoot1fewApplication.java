package com.onefew.springboot;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.onefew.springboot")
public class DemoSpringBoot1fewApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoSpringBoot1fewApplication.class, args);
	}
}

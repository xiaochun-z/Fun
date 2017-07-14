package com.onefew.springboot;

import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class DemoSpringBoot1fewApplicationTests {

	@Test
	public void contextLoads() {
	}

	@Autowired
	private UserDao userDao;

	@Test
	public void findById() throws Exception{
		User u = userDao.findById(1);
		Assert.assertEquals("Tom",u.getName());
	}
}

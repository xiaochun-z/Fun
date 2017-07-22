package com._1b2m.springbootfileuploadwithjqury

import org.springframework.boot.builder.SpringApplicationBuilder
import org.springframework.boot.web.support.SpringBootServletInitializer

class ServletInitializer : SpringBootServletInitializer() {

	override fun configure(application: SpringApplicationBuilder) : SpringApplicationBuilder {
		return application.sources(SpringBootFileUploadWithJquryApplication::class.java)
	}

}

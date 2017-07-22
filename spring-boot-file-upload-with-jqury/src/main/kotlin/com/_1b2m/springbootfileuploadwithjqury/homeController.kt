package com._1b2m.springbootfileuploadwithjqury

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.core.env.Environment
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*
import org.springframework.web.multipart.MultipartFile
import java.io.BufferedOutputStream
import java.io.File
import java.io.FileOutputStream
import java.nio.file.Paths

@Controller
@RequestMapping("/")
class homeController {
    @Autowired
    private lateinit var env: Environment

    @GetMapping("/")
    fun index(): String {
        return "index"
    }

    @ResponseBody
    @RequestMapping(value = "upload", method = arrayOf(RequestMethod.POST), consumes = arrayOf("multipart/form-data"))
    fun upload(@RequestPart("upload-file") uploadfile: Array<MultipartFile>): UploadResult {
        if (uploadfile.count() == 0) return UploadResult(false, "the uploading file is not detected.", arrayOf())

        val dir = env.getProperty("com._1b2m.defaultuploaddir")
        val f: File = File(dir)
        if (!f.exists()) {
            f.mkdirs()
        }

        for (file in uploadfile) {
            val fileName = file.originalFilename;

            val filepath: String = Paths.get(dir, fileName).toString()
            val stream: BufferedOutputStream = BufferedOutputStream(FileOutputStream(File(filepath)))
            stream.write(file.bytes)
            stream.close()
        }

        return UploadResult(true, "successfully uploaded your file(s). ", uploadfile.map { it.originalFilename }.toTypedArray())
    }


}

class UploadResult(val success: Boolean, val message: String, val files: Array<String>)

using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Caching;
using System.Threading;
using System.Web;
using System.Web.Mvc;
using Microsoft.AspNet.SignalR;

namespace WebApplication1.Controllers
{

    public class PushController : Controller
    {
        private static readonly object locker = new object();


        public void GetMessage()
        {
            Response.ContentType = "text/event-stream";
            Response.AddHeader("Cache-Control", "no-cache");
            string message = MemoryCache.Default.Get("server-push-message")?.ToString();
            if (!string.IsNullOrEmpty(message))
            {
                lock (locker)
                {
                    if (!string.IsNullOrEmpty(message))
                    {
                        MemoryCache.Default.Remove("server-push-message");
                        Response.Write($"data:{message}\n\n");
                    }
                }

            }

            Response.Flush();

        }
    }

    public static class MessagePushHelper
    {

        public static void PushMessage(string message)
        {
            MemoryCache.Default.Set("server-push-message", message, DateTimeOffset.MaxValue);
        }

        public static void PushSignalR(string message)
        {
            GlobalHost.ConnectionManager.GetHubContext<MessageHub>().Clients.All.addNewMessageToPage(message);
        }
    }

    public class MessageHub : Hub
    {
    }


    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }

        public ActionResult GetFoo()
        {
            ComplexBusiness.InvokeFooReturnInt();
            return new EmptyResult();
        }

        public ActionResult GetFooSignalR()
        {
            ComplexBusiness.InvokeFoo();
            return new EmptyResult();
        }
    }

    public class MessageResult
    {
        public string Message { get; set; }
    }



    public class ComplexBusiness
    {
        public static string GetFoo()
        {
            return "";
        }

        public static void InvokeFoo()
        {
            MessagePushHelper.PushSignalR($"服务器当前时间：{DateTime.Now}");
        }

        public static int InvokeFooReturnInt()
        {
            MessagePushHelper.PushMessage($"服务器当前时间：{DateTime.Now}");
            return 0;
        }
    }
}
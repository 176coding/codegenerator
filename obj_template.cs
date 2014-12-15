using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ArtOfTest.WebAii.Core;
using ArtOfTest.WebAii.ObjectModel;
using ArtOfTest.WebAii.TestAttributes;
using ArtOfTest.WebAii.TestTemplates;
using ArtOfTest.WebAii.Controls.HtmlControls;


public class ${class_name} : HtmlPage
{
	private Browser _ownerBrowser;
	public ${class_name}(string url, Find find) :
		base(url, find)
	{
		this._ownerBrowser = find.AssociatedBrowser;
	}
	
	
	//private region
	${private_property}
	
	private string TagA = "tagname=a";
	private string TagInput = "tagname=input";
	private string TagSelect = "tagname=select";
	
	//frame inner class
	//in another template file
	
	//public region
	${public_property}
	
	
	
}

  
  


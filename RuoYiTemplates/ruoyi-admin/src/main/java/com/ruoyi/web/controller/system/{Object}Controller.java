package com.ruoyi.web.controller.system;

import java.util.List;
import org.apache.shiro.authz.annotation.RequiresPermissions;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import com.ruoyi.common.annotation.Log;
import com.ruoyi.common.enums.BusinessType;
import com.ruoyi.system.domain.{Object};
import com.ruoyi.system.service.I{Object}Service;
import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.page.TableDataInfo;
import com.ruoyi.common.core.domain.AjaxResult;
import com.ruoyi.common.utils.poi.ExcelUtil;

/**
 * 部门 信息操作处理
 * 
 * @author ruoyi
 * @date 2019-06-19
 */
@Controller
@RequestMapping("/system/{object}")
public class {Object}Controller extends BaseController
{
    private String prefix = "system/{object}";
	
	@Autowired
	private I{Object}Service {object}Service;
	
	@RequiresPermissions("system:{object}:view")
	@GetMapping()
	public String {object}()
	{
	    return prefix + "/{object}";
	}
	
	/**
	 * 查询部门列表
	 */
	@RequiresPermissions("system:{object}:list")
	@PostMapping("/list")
	@ResponseBody
	public TableDataInfo list({Object} {object})
	{
		startPage();
        List<{Object}> list = {object}Service.select{Object}List({object});
		return getDataTable(list);
	}
	
	
	/**
	 * 导出部门列表
	 */
	@RequiresPermissions("system:{object}:export")
    @PostMapping("/export")
    @ResponseBody
    public AjaxResult export({Object} {object})
    {
    	List<{Object}> list = {object}Service.select{Object}List({object});
        ExcelUtil<{Object}> util = new ExcelUtil<{Object}>({Object}.class);
        return util.exportExcel(list, "{object}");
    }
	
	/**
	 * 新增部门
	 */
	@GetMapping("/add")
	public String add()
	{
	    return prefix + "/add";
	}
	
	/**
	 * 新增保存部门
	 */
	@RequiresPermissions("system:{object}:add")
	@Log(title = "部门", businessType = BusinessType.INSERT)
	@PostMapping("/add")
	@ResponseBody
	public AjaxResult addSave({Object} {object})
	{		
		return toAjax({object}Service.insert{Object}({object}));
	}

	/**
	 * 修改部门
	 */
	@GetMapping("/edit/{{object}Id}")
	public String edit(@PathVariable("{object}Id") Long {object}Id, ModelMap mmap)
	{
		{Object} {object} = {object}Service.select{Object}ById({object}Id);
		mmap.put("{object}", {object});
	    return prefix + "/edit";
	}
	
	/**
	 * 修改保存部门
	 */
	@RequiresPermissions("system:{object}:edit")
	@Log(title = "部门", businessType = BusinessType.UPDATE)
	@PostMapping("/edit")
	@ResponseBody
	public AjaxResult editSave({Object} {object})
	{		
		return toAjax({object}Service.update{Object}({object}));
	}
	
	/**
	 * 删除部门
	 */
	@RequiresPermissions("system:{object}:remove")
	@Log(title = "部门", businessType = BusinessType.DELETE)
	@PostMapping( "/remove")
	@ResponseBody
	public AjaxResult remove(String ids)
	{		
		return toAjax({object}Service.delete{Object}ByIds(ids));
	}
	
}
